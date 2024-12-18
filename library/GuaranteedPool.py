import json, os, shutil, sys, random
import datetime
from .GUIcomponents import output
from .Member import *

RECORD_NEEDED_TO_GUARANTEE = 2
INTERVAL_LIMIT:datetime.timedelta = datetime.timedelta(days = 180)
DATE_FORMAT = "%Y-%m-%d"
CURRENT_DATE:datetime.date = datetime.datetime.now().date()

class GuaranteedPool(object):
    __members: dict[str, GuaranteedMember] = {}
    def __init__(self, activityTime:str, baseDir:str = None) -> None:
        self.__members.clear()
        self.__activity_time = activityTime
        self.__baseDir = baseDir
        self.__guarantee_data_path = os.path.normpath(os.path.join(self.__baseDir, "data", "guarantee_data.json"))
        if not self.__load_data(self.__guarantee_data_path):
            sys.exit()

    def __load_data(self, guarantee_data_file:str) -> bool:
        try:
            self.__members.clear()
            with open(guarantee_data_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                members = data.get('members', [])
                for member in members:
                    wechatId = member.get('wechat_id', '?')
                    member = GuaranteedMember( 
                        wechat_id = wechatId,
                        name = member.get('name', '?'),
                        record = member.get('record', 0),
                        lastEnrolledDate = datetime.datetime.strptime(member.get('last_enrolled_date', CURRENT_DATE.strftime(DATE_FORMAT)), DATE_FORMAT).date(),
                        missedActivities = member.get('missed_activities', list()),
                        lastParticipatedActivity = member.get('last_participated_activity', str())
                    )
                    self.__members[wechatId] = member
                if(self.__activity_time == data.get('last_modified_time','')):
                    output("该活动已经抽签过，请勿重复抽签，如需重新抽签请恢复上一次保底文件")
                    return False
                return True
        except FileNotFoundError:
            output(f"File {guarantee_data_file} not found.")
            return False
        except json.JSONDecodeError:
            output("Error decoding JSON.")
            return True

    def __is_guarantee(self, wechatID:str) -> bool:
        if not wechatID in self.__members:
            return False
        return self.__members[wechatID].getRecord() >= RECORD_NEEDED_TO_GUARANTEE

    def __add_record(self, wechatID:str, name:str) -> None:
        if wechatID in self.__members:
            self.__members[wechatID].addRecord()
            self.__members[wechatID].setName(name)
        else:
            self.__members[wechatID] = GuaranteedMember(name = name, wechat_id = wechatID, record=1)

    def __clear_record(self, wechatID:str) -> None:
        if wechatID in self.__members:
            self.__members[wechatID].clearRecord()

    def saveData(self) -> None:
        data = {
            'last_modified_time':self.__activity_time, # 存储当前时间
            'members':[]
        }
        for wechatId, member in self.__members.items():
            data['members'].append({
                'wechat_id':wechatId,
                'name':member.getName(),
                'record':member.getRecord(),
                'last_enrolled_date':member.getLastEnrolledDate().strftime(DATE_FORMAT),
                'missed_activities':member.getMissedActivities(),
                'last_participated_activity':member.getLastParticipatedActivity(),
            })
        with open(self.__guarantee_data_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        new_file_name = 'data_' + self.__activity_time + '.json'
        guarantee_history_dir_path = os.path.join(self.__baseDir, "GuaranteeHistory")
        if not os.path.exists(guarantee_history_dir_path):
            os.mkdir(guarantee_history_dir_path)
        destination_file = os.path.join(guarantee_history_dir_path, new_file_name)
        shutil.copy2(self.__guarantee_data_path, destination_file)

    def getPreviligedMembers(self, enrolledMembers:set[EnrolledMember], Nbound:int) -> set[EnrolledMember]:
        previliged_members:list[EnrolledMember] = []
        for member in enrolledMembers:
            if self.__is_guarantee(member.getWechatID()):
                member.record = self.__members[member.getWechatID()].getRecord()
                previliged_members.append(member)
        previliged_members.sort(key = lambda x: (x.record, random.random()), reverse = True)
        if(len(previliged_members) > Nbound):
            output("保底名单人数超过限制，共有%d人" % len(previliged_members))
            previliged_members = previliged_members[:Nbound]
        for member in previliged_members:
            member.tagGuaranteed()
        return set(previliged_members)

    def __update_last_enrolled_date(self, wechatID:str, name:str, date:datetime.date) -> None:
        if wechatID in self.__members:
            self.__members[wechatID].setName(name)
            self.__members[wechatID].setLastEnrolledDate(date)
        else:
            self.__members[wechatID] = GuaranteedMember(name = name, wechat_id = wechatID, record=0)
            self.__members[wechatID].setLastEnrolledDate(date)
    
    def __clear_missed_activities(self, wechatID:str) -> None:
        if wechatID in self.__members:
            self.__members[wechatID].clearMissedActivities()
    
    def __add_missed_activity(self, wechatID:str, name:str, activity:str) -> None:
        if wechatID in self.__members:
            self.__members[wechatID].addMissedActivities(activity)
        else:
            self.__members[wechatID] = GuaranteedMember(name = name, wechat_id = wechatID, record=0)
            self.__members[wechatID].addMissedActivities(activity)
    
    def __update_last_participated_activity(self, wechatID:str, name:str, activityTime:str):
        if wechatID in self.__members:
            self.__members[wechatID].setName(name)
            self.__members[wechatID].setLastParticipatedActivity(activityTime)
        else:
            self.__members[wechatID] = GuaranteedMember(name = name, wechat_id = wechatID, record=0)
            self.__members[wechatID].setLastParticipatedActivity(activityTime)
    
    def update(self, drawnMembers:set[EnrolledMember], undrawnMembers:set[EnrolledMember]) -> None:
        for drawn_member in drawnMembers:
            wechatID = drawn_member.getWechatID()
            name = drawn_member.getName()
            self.__clear_record(wechatID)
            self.__clear_missed_activities(wechatID)
            self.__update_last_enrolled_date(wechatID, name, CURRENT_DATE)
            self.__update_last_participated_activity(wechatID, name, self.__activity_time)
        for undranwn_member in undrawnMembers:
            wechatID = undranwn_member.getWechatID()
            name = undranwn_member.getName()
            self.__add_record(wechatID, name)
            self.__add_missed_activity(wechatID, name, self.__activity_time)
            self.__update_last_enrolled_date(wechatID, name, CURRENT_DATE)
        members_to_remove:list[str] = []
        for member in self.__members.values():
            if CURRENT_DATE - member.getLastEnrolledDate() > INTERVAL_LIMIT:
               members_to_remove.append(member.getWechatID())
        for wechatID in members_to_remove:
            self.__members.pop(wechatID)
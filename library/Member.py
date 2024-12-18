import datetime
class Member(object):
    def __init__(self, name:str, wechat_id:str) -> None:
        self._name:str = name
        self._wechat_id:str = wechat_id
    
    def getName(self) -> str:
        return self._name
    
    def getWechatID(self) -> str:
        return self._wechat_id


class GuaranteedMember(Member):
    def __init__(self, name:str, wechat_id:str, record:int, lastEnrolledDate:datetime.date = (datetime.datetime.now()).date(), missedActivities:list[str] = None, lastParticipatedActivity:str = None) -> None:
        super().__init__(name, wechat_id)
        self._record:int = record
        self._last_enrolled_date:datetime.date = lastEnrolledDate
        self._last_participated_activity:str = lastParticipatedActivity
        self._missed_activities:list[str] = missedActivities if missedActivities is not None else []
    
    def addRecord(self) -> None:
        self._record += 1
    
    def getRecord(self) -> int:
        return self._record
    
    def getName(self) -> str:
        return super().getName()
    
    def getWechatID(self) -> str:
        return super().getWechatID()
    
    def setName(self, name:str) -> None:
        self._name = name

    def clearRecord(self) -> None:
        self._record = 0
    
    def popMissedActivities(self) -> str:
        return self._missed_activities.pop()
    
    def addMissedActivities(self, activity:str) -> None:
        self._missed_activities.append(activity)

    def getLastEnrolledDate(self) -> datetime.date:
        return self._last_enrolled_date
    
    def setLastEnrolledDate(self, date:datetime.date) -> None:
        self._last_enrolled_date = date
    
    def clearMissedActivities(self) -> None:
        self._missed_activities.clear()
    
    def setLastParticipatedActivity(self, activity:str) -> None:
        self._last_participated_activity = activity

    def getMissedActivities(self) -> list[str]:
        return self._missed_activities
    
    def getLastParticipatedActivity(self) -> str:
        return self._last_participated_activity


class EnrolledMember(Member):
    def __init__(self, name:str, wechat_id:str, group_name:str, email_address:str, isGuaranteed:bool = False) -> None:
        super().__init__(name, wechat_id)
        self._group_name:str = group_name
        self._email_address:str = email_address
        self.is_guaranteed:str = isGuaranteed

    def getGroupName(self) -> str:
        return self._group_name
    
    def getGradeAndDepartment(self) -> str:
        return self._grade_and_department
    
    def getEmailAddress(self) -> str:
        return self._email_address
    
    def getWechatID(self) -> str:
        return super().getWechatID()
    
    def getName(self) -> str:
        return super().getName()
    
    def isGuaranteed(self) -> bool:
        return self.is_guaranteed
    
    def tagGuaranteed(self) -> None:
        self.is_guaranteed = True
Requirement:[
    {
        "id": 4,
        "name": "All Test Data",
        "status": "常态化",
        "description": "",
        "priority": 0,
        "created_at": "2024-05-20T10:37:39.781732Z",
        "updated_at": "2024-05-25T20:35:18.931400Z",
        "start_time": null,
        "end_time": null,
        "parents": [
            3,
            2,
            26,
            27
        ]
    },
    {
        "id": 25,
        "name": "Test Requirement 1",
        "status": "常态化",
        "description": "Description 1",
        "priority": 1,
        "created_at": "2024-05-20T13:39:52.148722Z",
        "updated_at": "2024-05-20T13:39:52.148722Z",
        "start_time": null,
        "end_time": null,
        "parents": [
            27
        ]
    },
    {
        "id": 26,
        "name": "Test Requirement 2",
        "status": "进行中",
        "description": "Description 2",
        "priority": 2,
        "created_at": "2024-05-20T13:39:52.267830Z",
        "updated_at": "2024-05-20T13:39:52.267830Z",
        "start_time": null,
        "end_time": null,
        "parents": [
            27
        ]
    },
]

Person:[
    {
        "id":1,
        "lName":"zack",
        "mid":"some mid",
        "fName":"Lin",
        "hometown":"",
        "description":"",
        "relationships":[],//type:relationship
        "create_time":"",
        "update_time":"",
    },
]

SocialRelationship:[
    {
        "id":"",
        "fromId":"1",
        "toId":"2",
        "Relation":"Sometext", //some type of relationship
    }
]

MediaAccount:[
    {
        "Media":"Wechat",
        "MediaAccount":"Ashcoto02",
    }
]

RelatedTodos:[
    {
        "id":1,
        "TodoId":1,
        "EventId":1,
    }
]

Media:[
    {
        "person":1,
        "media":"Wechat",
        "account":"Ashcoto0002",
    }
]
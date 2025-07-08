# 通用业务数据接口说明

## 1. 获取区域推荐房间列表

**说明**：获取Bigo平台推荐的区域房间集合列表。使用sign方式鉴权

**频率控制**：全平台 2000/s，单人5/s

**API：**

```
POST https://{{host_domain}}/sign/broom/get_country_list
Content-type: application/json
bigo-oauth-signature: {{sign}}
bigo-timestamp: {{timestamp}}
bigo-client-id: {{clientid}}


{{postdata}}
```



**头部说明：**

bigo-oauth-signature：签名验证方式sign

**请求参数说明：**

| **参数**   | **类型** | **是否必填** | **说明**                                                     |
| ---------- | -------- | ------------ | ------------------------------------------------------------ |
| seqid      | string   | 是           | 请求识别id，建议保证唯一性                                   |
| timestamp  | int64    | 是           | ms时间戳                                                     |
| ip         | string   | 是           | ip信息                                                       |
| lang       | string   | 否           | 语言                                                         |
| version    | string   | 否           | 客户端版本                                                   |

**返回参数说明：**

| **参数** | **类型**   | **说明**                                                     |
| -------- | --------   | ------------------------------------------------------------ |
| seqid    | string     | 原封不动返回请求的seqid                                      |
| rescode  | int        | 200：成功 400：请求参数异常 401：达到调用频限 500：平台异常，可重试 |
| messge   | string     | 具体错误说明                                                 |
| list     | json array | 房间信息列表，详见下图数据说明 |

```
"list":[
    {
        "cover_url":"https://xxx1",  //直播间封面
        "title":"test1",             //直播间标题
        "user_count":10,             //直播间人数
        "onelink":"https://bigo.onelink.me/1168916328?af_xp=referral&pid=xiaomi&is_retargeting=true&af_reengagement_window=30d&c=xxxxx&af_dp=bigolive%3A%2F%2Flivevideoshow%3Froomid%3D123456789%26uid%3D1111111"
    },
    {
        "cover_url":"https://xxx2",  //直播间封面
        "title":"test2",             //直播间标题
        "user_count":100,            //直播间人数
        "onelink":"https://bigo.onelink.me/1168916328?af_xp=referral&pid=xiaomi&is_retargeting=true&af_reengagement_window=30d&c=xxxxx&af_dp=bigolive%3A%2F%2Flivevideoshow%3Froomid%3D123456780%26uid%3D1111112"
    }
]
```

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
| country    | string   | 是           | 国家码
| lang       | string   | 否           | 语言                                                         |
| version    | string   | 否           | 客户端版本                                                   |

**返回参数说明：**

| **参数** | **类型**   | **说明**                                                     |
| -------- | --------   | ------------------------------------------------------------ |
| seqid    | string     | 原封不动返回请求的seqid                                      |
| rescode  | int        | 200：成功 400：请求参数异常 401：达到调用频限 500：平台异常，可重试 |
| message  | string     | 具体错误说明                                                 |
| list     | json array | 房间信息列表，详见下图数据说明 |

```
"list":[
    {
        "cover_url":"https://xxx1",  //直播间封面
        "title":"test1",             //直播间标题
        "user_count":10,             //直播间人数
        "onelink":"https://abcd1"    //直播间跳转链接
    },
    {
        "cover_url":"https://xxx2",  //直播间封面
        "title":"test2",             //直播间标题
        "user_count":100,            //直播间人数
        "onelink":"https://abcd2"    //直播间跳转链接
    }
]
```

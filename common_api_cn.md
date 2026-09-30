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

## 2. 批量获取用户基础信息

**说明**：根据一组用户的openid，批量获取对应用户的头像、昵称和性别。使用sign方式鉴权。

**数量限制**：每次请求传入1–20个openid，超过20个时需分批请求；数组为空或超过20个时返回rescode 400。

**API：**

```
POST https://{{host_domain}}/sign/user/batch_get_user_info
Content-type: application/json
bigo-oauth-signature: {{sign}}
bigo-timestamp: {{timestamp}}
bigo-client-id: {{clientid}}

{{postdata}}
```

**头部说明：**

| **头部类型** | **说明** |
| ------------ | -------- |
| bigo-oauth-signature | 签名验证方式sign，签名生成规则参考[服务端签名鉴权验证](./BIGOLIVEOpenPlatformAccessGuide_CN.md#三服务端签名鉴权验证) |
| bigo-timestamp | 秒级时间戳 |
| bigo-client-id | 业务唯一标识，由Bigo平台分配 |

**请求参数说明：**

| **参数** | **类型** | **是否必填** | **说明** |
| -------- | -------- | ------------ | -------- |
| seqid | string | 是 | 请求识别id，建议保证唯一性 |
| timestamp | int64 | 是 | ms时间戳 |
| openids | string array | 是 | 用户openid列表，至少1个，最多20个 |

**请求示例：**

```json
{
    "seqid": "batch_user_info_001",
    "timestamp": 1790726400000,
    "openids": ["openidA", "openidB"]
}
```

**返回参数说明：**

| **参数** | **类型** | **说明** |
| -------- | -------- | -------- |
| seqid | string | 原封不动返回请求的seqid |
| rescode | int | 200：成功；400：请求参数异常（包括openid数量不在1–20范围内）；401：达到调用频限；500：平台异常，可重试 |
| message | string | 具体错误说明 |
| list | json array | 用户信息列表，每项字段见下表，通过openid关联请求中的用户 |

**用户信息字段：**

| **参数** | **类型** | **说明** |
| -------- | -------- | -------- |
| openid | string | 用户的openid |
| nick_name | string | 用户昵称 |
| avatars | json | 用户头像，包含medium、small、big三个尺寸的头像URL |
| gender | string | 用户性别："0"：男；"1"：女；"2"：未知/保密；"3"：非二元性别 |

**返回示例：**

```json
{
    "seqid": "batch_user_info_001",
    "rescode": 200,
    "message": "success",
    "list": [
        {
            "openid": "openidA",
            "nick_name": "用户A",
            "avatars": {
                "medium": "https://example.com/avatar_a_medium.png",
                "small": "https://example.com/avatar_a_small.png",
                "big": "https://example.com/avatar_a_big.png"
            },
            "gender": "0"
        },
        {
            "openid": "openidB",
            "nick_name": "用户B",
            "avatars": {
                "medium": "https://example.com/avatar_b_medium.png",
                "small": "https://example.com/avatar_b_small.png",
                "big": "https://example.com/avatar_b_big.png"
            },
            "gender": "1"
        }
    ]
}
```

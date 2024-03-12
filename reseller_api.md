## 1. Reseller Diamond Recharge

Description: API for using the dealer's quota to recharge user with diamond, should using server-side signature to authenticate.

And for safe, 3rd should provide the account bigoid that needs to be deducted, and we need to bind it with client_id. And 3rd should provide server IPs to Bigo, the API only can be called in the server IPs.

**API:**

```
POST https://{{host_domain}}/sign/agent/rs_recharge

Content-type: application/json
bigo-oauth-signature: {{bigo-oauth-signature}}
bigo-client-id: {{client_id}}
bigo-oauth-signature: {{bigo-oauth-signature}}
bigo-timestamp: {{timestamp}}

{{postdata}}
```



**1.1. Header description:**

Reference [3.1.3. Step 3: Call Api with Signature](./BIGOLIVEOpenPlatformAccessGuide.md#313-step-3-call-api-with-signature)

**1.2. Request** **postdata** **parameter description:** 

| **Parameter**   | **Type** | **required** | **Description**                                              |
| --------------- | -------- | ------------ | ------------------------------------------------------------ |
| recharge_bigoid | string   | Y            | bigo_id that need to be recharged                            |
| reseller_bigoid | string   | N            | reseller's bigoid that whose credit needs to be deducted. If not filled, Bigo will deduct the default reseller's account. |
| seqid           | string   | Y            | Request serial number, should be unique, easier to track request. Only contain numbers and lowercase letters. The length must be between 13 and 32 |
| bu_orderid      | string   | Y            | 3rd business recharge orderid, should be unique.Only contain numbers, uppercase and lowercase letters, and underscores. The length must be no more than 40 |
| value           | int      | Y            | diamond amount required to be recharged                      |
| total_cost      | double   | Y            | the payment fee for users to recharge diamonds; the incoming value can have up to two decimal points. The value must be no more than 99999999999.00 |
| currency        | string   | Y            | The currency used by the user for payment, only the following currencies are supported, refer to **Supported currencies** |

**Supported currencies**: USD, CNY, TWD, MYR, THB, TRY, PHP, AUD, IDR, KRW, INR, HKD, SGD, MMK, JPY, EUR, NGN, DKK, UAH, ILS, IQD, RUB, BGN, HRK, CHF, CAD, GHS, HUF, ZAR, QAR, KZT, COP, CRC, TZS, EGP, RSD, MXN, BDT, PKR, PYG, BRL, NOK, CZK, MAD, LKR, NZD, CLP, GEL, SAR, PLN, MOP, BOB, SEK, GBP, PEN, JOD, RON, KES, VND, DZD, AED, LBP

Example：

```
{
    "recharge_bigoid": "52900149",
    "reseller_bigoid": "inshhaa",
    "seqid": "83jyhm2784_089j",
    "value": 712,
    "totalCost": 711.90,
    "currency": "USD"
}
```



**1.3. Response parameter description:**

| **Parameter** | **Type** | **Description**                                 |
| ------------- | -------- | ----------------------------------------------- |
| seqid         | string   | is equal to the seqid of request                |
| rescode       | int      | response code, refer to followed table 'recode' |
| message       | String   | details of error                                |

rescode:

| **Value** | **Description**                                              |
| --------- | ------------------------------------------------------------ |
| 0         | Success                                                      |
| 400001    | The request parameter is illegal. For detailed information, see 'message' |
| 7212001   | The recharge API was disable by Bigo                         |
| 7212002   | The recharge API was disable by the third-party website      |
| 7212003   | The request source is not within the authorized IP           |
| 7212004   | recharge_bigoid is not existed                               |
| 7212005   | recharge_bigoid cannot be recharged                          |
| 7212006   | The reseller_bigoid is not bind with the client_id           |
| 7212008   | The number of filled diamonds exceeds the upper limit        |
| 7212009   | 'currency' not supported, refer to **Supported currencies**  |
| 7212010   | orderid is duplicated                                        |
| 7212011   | insufficient balance                                         |
| 7212012   | request frequently, just wait a second to call               |
| 500001    | Other errors, contact Bigo team                              |



## 2. Recharge Precheck

Decription: Api for checking bigoid that will be recharged if it is legal and checking the resller_bigoid if it has sufficient balance before you call the 'Reseller Diamond Recharge' API.

**API:**

```
POST https://{{host_domain}}/sign/agent/recharge_pre_check

Content-type: application/json
bigo-oauth-signature: {{bigo-oauth-signature}}
bigo-client-id: {{client_id}}
bigo-oauth-signature: {{bigo-oauth-signature}}
bigo-timestamp: {{timestamp}}

{{postdata}}
```



**2.1. Header description:**

Reference [3.1.3. Step 3: Call Api with Signature](./BIGOLIVEOpenPlatformAccessGuide.md#313-step-3-call-api-with-signature)



**2.2. Request** **postdata** **parameter description:** 

| **Parameter**   | **Type** | **required** | **Description**                                              |
| --------------- | -------- | ------------ | ------------------------------------------------------------ |
| recharge_bigoid | string   | Y            | bigo_id that need to be recharged                            |
| reseller_bigoid | string   | N            | reseller's bigoid that whose credit needs to be deducted. If not filled, Bigo will deduct the default reseller's account. |
| seqid           | string   | Y            | Request serial number, should be unique, easier to track request. Only contain numbers and lowercase letters. The length must be between 13 and 32 |



**2.3. Response parameter description:**

| **Parameter**    | **Type** | **Description**                              |
| ---------------- | -------- | -------------------------------------------- |
| seqid            | string   | is equal to the seqid of request             |
| rescode          | int      | response code, refer to 2.3.1 'recode' table |
| message          | String   | details of error                             |
| recharge_balance | int      | diamond's balance of reseller                |



## 3. Disable Recharge

Decription: Disable all the recharge API when you are necessary, such as your website is under attack or serious logic errors were occurred in your website . But if you want to enable again, you only should contact Bigo to turn on the switch.

**API:**

```
POST https://{{host_domain}}/sign/agent/disable

Content-type: application/json
bigo-oauth-signature: {{bigo-oauth-signature}}
bigo-client-id: {{client_id}}
bigo-oauth-signature: {{bigo-oauth-signature}}
bigo-timestamp: {{timestamp}}

{{postdata}}
```



**3.1. Header description:**

Reference [3.1.3. Step 3: Call Api with Signature](./BIGOLIVEOpenPlatformAccessGuide.md#313-step-3-call-api-with-signature)



**3.2. Request** **postdata** **parameter description:** 

| **Parameter** | **Type** | **required** | **Description**                                              |
| ------------- | -------- | ------------ | ------------------------------------------------------------ |
| seqid         | string   | Y            | Request serial number, should be unique, easier to track request. Only contain numbers and lowercase letters. The length must be between 13 and 32 |



**3.3. Response parameter description:**

| **Parameter** | **Type** | **Description**                  |
| ------------- | -------- | -------------------------------- |
| seqid         | string   | is equal to the seqid of request |
| rescode       | int      | 0, success500001: other errors   |
| message       | String   | details of error                 |


---
title: BandSim
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
code_clipboard: true
highlight_theme: darkula
headingLevel: 2
generator: "@tarslib/widdershins v4.0.29"

---

# BandSim

Base URLs:

# Authentication

- HTTP Authentication, scheme: bearer

# Default

## POST 微信快速登录

POST /api/v1/auth/wechat

> Body 请求参数

```json
{
  "code": "微信临时登录码"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» code|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "message": "string",
  "data": {
    "token": "string",
    "user": {
      "userId": "string",
      "nickname": "string",
      "avatarUrl": "string"
    }
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» message|string|true|none||none|
|» data|object|true|none||none|
|»» token|string|true|none||none|
|»» user|object|true|none||none|
|»»» userId|string|true|none||none|
|»»» nickname|string|true|none||none|
|»»» avatarUrl|string|true|none||none|

状态码 **400**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» message|string|true|none||none|
|» errors|object|true|none||none|
|»» code|string|true|none||none|

## POST 手机号注册

POST /api/auth/register

> Body 请求参数

```json
{
  "phone": "+8613800138000",
  "code": "短信验证码"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» phone|body|string| 是 |none|
|» code|body|string| 是 |none|

> 返回示例

```json
{
  "code": 201,
  "message": "注册成功",
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "user_id": "456"
  }
}
```

```json
{
  "code": 409,
  "message": "手机号已注册",
  "errors": {
    "phone": "该手机号已被使用"
  }
}
```

```json
{
  "code": 404,
  "message": "手机号不存在",
  "errors": {
    "phone": "该手机号错误"
  }
}
```

> 404 Response

```json
{
  "code": 0,
  "message": "string",
  "errors": {
    "phone": "string"
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|none|Inline|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» message|string|true|none||none|
|» data|object|true|none||none|
|»» token|string|true|none||none|
|»» userId|string|true|none||none|

状态码 **404**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» message|string|true|none||none|
|» errors|object|true|none||none|
|»» phone|string|true|none||none|

状态码 **409**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» message|string|true|none||none|
|» errors|object|true|none||none|
|»» phone|string|true|none||none|

## POST 发送短信验证码

POST /api/auth/sms-code

> Body 请求参数

```json
"{\r\n  \"phone\": \"+8613800138000\",\r\n  \"type\": \"register\" // enum: register/login/reset\r\n}"
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» phone|body|string| 是 |none|
|» type|body|string| 是 |enum: register/login/reset|

> 返回示例

```json
{
  "code": 200,
  "message": "验证码已发送",
  "data": {
    "expires_in": 300
  }
}
```

```json
{
  "code": 429,
  "message": "请求过于频繁",
  "errors": {
    "retry_after": 60
  }
}
```

> 429 Response

```json
{
  "code": 0,
  "message": "string",
  "errors": {
    "retryAfter": 0
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|429|[Too Many Requests](https://tools.ietf.org/html/rfc6585#section-4)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» message|string|true|none||none|
|» data|object|true|none||none|
|»» expiresIn|integer|true|none||none|

状态码 **429**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» message|string|true|none||none|
|» errors|object|true|none||none|
|»» retryAfter|integer|true|none||none|

## POST 密码登录

POST /api/auth/login

> Body 请求参数

```json
{
  "phone": "+8613800138000",
  "password": "your_password"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» phone|body|string| 是 |none|
|» password|body|string| 是 |none|

> 返回示例

```json
{
  "code": 200,
  "message": "登录成功",
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "user_id": "789"
  }
}
```

> 401 Response

```json
{
  "code": 0,
  "message": "string",
  "errors": {
    "password": "string"
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» message|string|true|none||none|
|» data|object|true|none||none|
|»» token|string|true|none||none|
|»» userId|string|true|none||none|

状态码 **401**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» message|string|true|none||none|
|» errors|object|true|none||none|
|»» password|string|true|none||none|

## POST 退出登录

POST /api/auth/logout

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|  Authorization|header|string| 否 |none|

> 返回示例

```json
{
  "code": 200,
  "message": "已退出登录"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» message|string|true|none||none|

## GET 生成设备配对二维码

GET /api/devices/pairing-qrcode

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|Authorization|header|string| 否 |none|

> 返回示例

```json
{
  "code": 200,
  "data": {
    "qrcode_url": "https://api.example.com/qrcode/6A3B9C",
    "expires_in": 300
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» data|object|true|none||none|
|»» qrcodeUrl|string|true|none||none|
|»» expiresIn|integer|true|none||none|

## POST 扫码绑定设备

POST /api/devices/bind

> Body 请求参数

```json
{
  "pairing_code": "{{pairing_code}}"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|Authorization|header|string| 否 |none|
|body|body|object| 否 |none|
|» pairingCode|body|string| 是 |none|

> 返回示例

```json
{
  "code": 201,
  "message": "设备绑定成功",
  "data": {
    "device_id": "device_abc123",
    "name": "我的智能手环",
    "sn": "SN123456789"
  }
}
```

> 410 Response

```json
{
  "code": 0,
  "message": "string",
  "errors": {
    "pairingCode": "string"
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|410|[Gone](https://tools.ietf.org/html/rfc7231#section-6.5.9)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» message|string|true|none||none|
|» data|object|true|none||none|
|»» deviceId|string|true|none||none|
|»» name|string|true|none||none|
|»» sn|string|true|none||none|

状态码 **410**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» message|string|true|none||none|
|» errors|object|true|none||none|
|»» pairingCode|string|true|none||none|

## DELETE 解绑设备

DELETE /api/devices/{deviceId}

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|deviceId|path|string| 是 |none|
|Authorization|header|string| 否 |none|

> 返回示例

```json
{
  "code": 200,
  "message": "设备已解绑"
}
```

> 404 Response

```json
{
  "code": 0,
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» message|string|true|none||none|

状态码 **404**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» message|string|true|none||none|

## POST 实时流式上传数据

POST /api/health-data/stream

> Body 请求参数

```json
"[\r\n  {\r\n    \"type\": \"heart_rate\",\r\n    \"value\": 75,\r\n    \"timestamp\": 1620000000\r\n  },\r\n  // 更多数据项...\r\n]"
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|Authorization|header|string| 否 |none|
|body|body|array[object]| 否 |none|

> 返回示例

```json
{
  "code": 202,
  "message": "数据接收成功",
  "data": {
    "received_count": 50,
    "invalid_count": 2,
    "invalid_samples": [
      {
        "index": 3,
        "error": "心率值超出范围"
      }
    ]
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» message|string|true|none||none|
|» data|object|true|none||none|
|»» receivedCount|integer|true|none||none|
|»» invalidCount|integer|true|none||none|
|»» invalidSamples|[object]|true|none||none|
|»»» index|integer|false|none||none|
|»»» error|string|false|none||none|

## GET 获取数据可视化

GET /api/health-data/visualization

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|type|query|string| 是 |none|
|granularity|query|string| 是 |none|
|start_time|query|string| 否 |none|
|end_time|query|string| 否 |none|
|Authorization|header|string| 否 |none|

> 返回示例

```json
{
  "code": 200,
  "data": {
    "type": "steps",
    "granularity": "hour",
    "start_time": 1620000000,
    "end_time": 1620086400,
    "points": [
      {
        "timestamp": 1620000000,
        "value": 1200
      },
      {
        "timestamp": 1620003600,
        "value": 1500
      }
    ],
    "summary": {
      "total": 25000,
      "average": 3571
    }
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» data|object|true|none||none|
|»» type|string|true|none||none|
|»» granularity|string|true|none||none|
|»» startTime|integer|true|none||none|
|»» endTime|integer|true|none||none|
|»» points|[object]|true|none||none|
|»»» timestamp|integer|true|none||none|
|»»» value|integer|true|none||none|
|»» summary|object|true|none||none|
|»»» total|integer|true|none||none|
|»»» average|integer|true|none||none|

# 数据模型


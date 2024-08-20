import requests

headers = {
        'Host': 'api.classplusapp.com', 
        'origin': 'https://web.classplusapp.com', 
        'app-version': '1.4.39.5', 
        'api-version': '20', 
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.186 Safari/537.36', 
        'referer': 'https://web.classplusapp.com/login', 
        'device-id': "3Gjdj6hdhdjUi", 
    }

params = (
    ('platform', 'BROWSER'),
    ('type', 'MOVIE'),
)
# params inserted below will be passed to data-raw 

token = 'PFYtFSqWMYIROJYywBp0rbKvpD3z6N6E6UezNrZmCeKHkcJ5BiH4J8qwO0kfWOmrSsyFJMg9OqKKEwvuQiXL4qdDTa6ZYplNV9IQt6eEuveglDxjVlYd0vAecS5TZKn5mIs01YxcYNlTC7tu3BIk63JhMykMWEMmj1oEqaLa7N3ZrfU2VTlEPaWXBQV6PxnFeD022Yi298GOX/lDik7sXt5u4duT0aKIYbz0HPmjoh8b9Uy8bvzJUa0/SlgRcsW8RNTNjRJHM6N7BESCBGFEZcWoSXeDLEblEfRoBKro2iDGB1neLfRdY1fj7tJX1Rn9lj+OJwRTrBV4XoTQFuSsFwvYCeQfkAoRHXnze9njI5pY7sYgIGxuM4Zh3Wqaps6kxdO53QMm0jJ/L41X6r5CikSGKQ3Rcps8eQccZb9svEuyXMof2nm+eYL+AVPPrfmAf/BrmUHfiuF9CmNsF9pI7PjJfLeASmh3KDI/5gUuC4uJB7rjTzHVWNRz8MSvYjJ37/5V9+FTihpu04+0jFZ1AlGRks2dzk2IGvm5WcwUhsW2l/oQXlh7AgsksIl2DT0wH11WeG+h1/ijymMcG9AZzsxtkC53eLJ8bl55/Aag0TJfX4N6KvV7UhglXxkLifb06bLK/wlcGCfb01b4cnngcjPJEMxh2+Q7sJSnbyrtsfodzNah8JXITmx5kTkFFZkdtga1ha9jAb+Z40VMQfbrCLgh0GEe2G3VczcIt8QHAWAeS91TkzLbMRAugbgLvdbI8yQXtM15uo+TXrV4PNFprug33AnvnQu7IpNxlmgPMZhEn4Qqc/V++OFIpz/JYEMnLFvjYcXE2+sPc4uKnoE0xk33+IgZKtWtDhxRg2SJKyKOYxXucXybUuqPP/d+Nq1VNhD84Of+EfVvBjs1u75pNz/kmu5ms9ppRMkafq0/2311hbYi6VXmp6AeJweGJWkGKEFxw7xADuC8iM7xWnXW5aiNvhbsXBOwuTK8b2ioxjrg6OFhiMck+z9M5FHg+ktY7YB8iY+0V6B/Op2cQGtLaZ2E9lsomlQpxL+LiPI7UWEqmALEGH/Pk5tdLnlFRjEk2PPc8YURw+/nkP9tqJ/AXQwaXc9iwC5yxlYPCsp/Tc4='
provider = 'kakaotv'


releasePid = "_qVpiY31v_oU"
# response = requests.post('https://widevine-proxy.ott.yandex.ru/proxy', headers=headers, cookies=cookies, data=data)

# print(f'{chr(10)}widevine_license: {response.content}')
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.options('https://api.ott.kinopoisk.ru/v12/license-affected-content-metadata?contentIds=4b63db58ab27e92b90a457e533b00007&serviceId=25', headers=headers)
# dash-cenc/hdr10_uhd_hevc_ec3.mpd
# https://strm.yandex.ru/vh-ottenc-converted/vod-content/4315082489d87677b21f7c83593fcb73/8614535x1631802676x41611665-4e76-41ac-93a7-5070b77b5f3c/dash-cenc/sdr_uhd_hevc_ec3.mpd

# 'GET /certificate HTTP/1.1'

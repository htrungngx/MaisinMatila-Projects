import urequests, network

#sta_if = network.WLAN(network.STA_IF)
#sta_if.active(True)
#sta_if.connect('AIoT-Garage', 'asdfghjk')


def make_request(data, image=None):
    boundary = '---011000010111000001101001'
    #boundary fixed instead of generating new one everytime

    def encode_field(field_name): # prepares lines that include chat_id
        return (
            b'--%s' % boundary,
            b'Content-Disposition: form-data; name="%s"' % field_name,
            b'',
            b'%s'% data[field_name] #field_name conatains chat_id
        )


    def encode_file(field_name):  # prepares lines for the file
        filename = 'latest.bmp'  # dummy name is assigned to uploaded file
        return (
            b'--%s' % boundary,
            b'Content-Disposition: form-data; name="%s"; filename="%s"' % (
                field_name, filename),
            b'',
            image
        )

    lines = [] # empty array initiated
    for name in data:
        lines.extend(encode_field(name)) # adding lines (data)
    if image:
        lines.extend(encode_file('image')) # adding lines  image
    lines.extend((b'--%s--' % boundary, b'')) # ending  with boundary

    body = b'\r\n'.join(lines) # joining all lines constitues body
    body = body + b'\r\n' # extra addtion at the end of file

    headers = {
        'content-type': 'multipart/form-data; boundary=' + boundary
        }  # removed content length parameter
    return body, headers  # body contains the assembled upload package


def upload_image(url, headers, data):
    http_response = urequests.post(
        url,
        headers=headers,
        data=data
    )
    print(http_response.status_code) # response status code is the output for request made

    if (http_response.status_code == 204 or http_response.status_code == 200):
        print('Uploaded request')
    else:
        print('cant upload')
        #raise UploadError(http_response) line commneted out
    #http_response.close()
    return http_response


# funtion below is used to set up the file / photo to upload
def send_my_photo(photo_pathstring): #  path and filename combined
    #token = 'authentication token or other data' # this my bot token
    chat_id= 999999999 # my chat_id
    #url = 'http://192.168.1.115:3000' + token
    url = 'http://192.168.0.53:3000'
    path = photo_pathstring   # this is the local path
    myphoto = open(path , 'rb') #myphoto is the photo to send
    myphoto_data = myphoto.read() # generate file in bytes
    data = { 'timestamp' : 999999999 }
    body, headers  = make_request(data, myphoto_data) # generate body to upload
    url = url + '/upload'
    headers = { 'content-type': "multipart/form-data; boundary=---011000010111000001101001" }
    response = upload_image(url, headers, body) # using function to upload to telegram
    return response

#response = send_my_photo("latest.bmp")
#print(str(response.text))

import sensor, image, os, time

sensor.reset()                      # Reset and initialize the sensor.
sensor.set_pixformat(sensor.GRAYSCALE) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.HQVGA)   # Set frame size to HQVGA (240x160)
sensor.skip_frames(time = 2000)     # Wait for settings take effect.


def captureImage():
    i = sensor.snapshot()
    frameBuffer = sensor.get_fb()
    frameBuffer.save(os.getcwd()+'/latest.bmp') #save images as the lastest file
    time.sleep(2.5) #Wait 2.5 seconds before send confirmation
    print('Image captured and saved')
    return # Make sure the image is saved and then continue

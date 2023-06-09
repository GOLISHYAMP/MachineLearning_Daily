from threading import Thread

from time import sleep

import gi

gi.require_version("Gst","1.0")




from gi.repository import Gst, GLib, GObject




Gst.init()




main_loop = GLib.mainloop()

main_loop_thread = Thread(target=main_loop.run)

main_loop_thread.start()




pipeline = Gst.parse_launch("ksvideosrc ! decodebin !videoconvert ! autovideosink ")




pipeline.set_state(Gst.state.PLAYING)




try:

    while True:

        sleep(0.1)

except KeyboardInterrupt:

    pass




pipeline.set_state(Gst.state.NULL)

main_loop.quit()

main_loop_thread.join()



import inotify.adapters
from notifypy import Notify


def _main():
    i = inotify.adapters.Inotify() #creates a instance of notification watcher of files/folders

    notification = Notify() #creates a instance of desktop notification library
    i.add_watch('/tmp') 

    #testing modifying a file inside folder /tmp
    with open('/tmp/test_file', 'w'):
        pass

    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        notification.title = type_names
        notification.message = filename + " - " + path
        notification.send()

        print("PATH=[{}] FILENAME=[{}] EVENT_TYPES={}".format(
              path, filename, type_names))

if __name__ == '__main__':
    _main()
#!/usr/bin/env python
import json
import time
import argparse
from paprika.threads.Abort import Abort
from paprika.threads.Threads import Threads
from paprika.threads.Runner import Runner
from paprika.executors.WatchWorker import WatchWorker
from paprika.executors.LocationWatcher import LocationWatcher
from paprika.system.Finder import Finder
import paprika
import os


def main(args=None):
    # Instantiate the parser
    parser = argparse.ArgumentParser(description="paprika-scanner agent")
    parser.add_argument('-v', action='store_true', help='show the version')

    args = parser.parse_args(args)
    if args.v:
        print "paprika version " + paprika.__version__
        exit(0)

    properties = dict()
    properties['agent.dir'] = os.path.abspath(os.path.dirname(__file__))
    properties['current.dir'] = os.path.abspath('.')
    f = Finder.open(properties, 'paprika_scanner.json')
    settings = json.load(f)

    abort = Abort()
    threads = Threads(abort)
    t = Runner.run(WatchWorker(LocationWatcher(), settings, threads, abort))
    threads.append({'thread': t})

    try:
        while True:
            time.sleep(settings['agent_idle_delay'])
    except:
        threads.abort()

if __name__ == "__main__":
    main(args=None)



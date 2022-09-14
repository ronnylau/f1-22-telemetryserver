from argparse import ArgumentParser
from threading import Thread

from listener import PacketListener

import live
from collector import TelemetryCollector
from server import serve
from storage import InfluxDBSink
from storage import InfluxDBSinkError


DEFAULT_BUCKET = "f1-telemetry"


def main():
    argp = ArgumentParser(prog="f1-tel")

    argp.add_argument(
        "org",
        help="InfluxDB Org",
        type=str,
    )
    argp.add_argument(
        "token",
        help="InfluxDB Token",
        type=str,
    )
    argp.add_argument(
        "-b",
        "--bucket",
        help="InfluxDB Bucket",
        type=str,
        default=DEFAULT_BUCKET,
    )
    argp.add_argument(
        "-r",
        "--report",
        help="Generate reports at the end of sessions. Useful for session coordinators",
        action="store_true",
    )

    args = argp.parse_args()

    collector = None

    try:
        with InfluxDBSink(org=args.org, token=args.token, bucket=args.bucket) as sink:
            if not sink.connected:
                print(
                    "WARNING: InfluxDB not available. Telemetry data will not be stored."
                )
            else:
                print("Connected to InfluxDB")

            listener = PacketListener()
            collector = TelemetryCollector(listener, sink, args.report)

            server_thread = Thread(target=serve, args=(args.org, args.token))
            server_thread.daemon = True
            server_thread.start()

            print("Listening for telemetry data ...")
            collector_thread = Thread(target=collector.collect)
            collector_thread.daemon = True
            collector_thread.start()

            print("Starting live data websocket server")
            # FIXME: Mixing asyncio and threads is yuck!
            live.serve()

    except InfluxDBSinkError as e:
        print("Error:", e)

    except KeyboardInterrupt:
        if collector is not None:
            collector.flush()
        print("\nBOX BOX.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

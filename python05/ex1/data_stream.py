from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):
    stream_type = "DataStream"

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.print_all = True

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if (criteria is None):
            return data_batch
        try:
            types = {
                "int": int,
                "str": str,
                "float": float,
                "dict": dict
                }
            if criteria in types:
                return [i for i in data_batch
                        if (isinstance(i, types[criteria]))]
            return []
        except Exception:
            return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
        }


class SensorStream(DataStream):
    stream_type = "Environmental Data"

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            validated_data = [i for i in data_batch if isinstance(i, dict)]
            if self.print_all:
                batch_content = ""
                for i in validated_data:
                    for j in i:
                        if batch_content != "":
                            batch_content += ", "
                        batch_content += f"{j}:{i[j]}"
                print(f"Processing sensor batch: [{batch_content}]")
                total = 0
                count = 0
                alert = []
                for i in validated_data:
                    if "temp" in i:
                        total += i["temp"]
                        count += 1
                        if i["temp"] > 50:
                            alert.append(i["temp"])
                avg = total / count if count > 0 else 0.0
                msg = ""
                if alert:
                    msg = ", ".join(f"{i}°C" for i in alert)
                    msg = f" Alert: high temp [{msg}]"
                return (f"Sensor analysis: {len(validated_data)} readings "
                        f"processed, avg temp: {avg}°C{msg}")
            return f"Sensor data: {len(validated_data)} readings processed"
        except Exception:
            return ("Error in SensorStream processing")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "critical":
            res = []
            for i in data_batch:
                if isinstance(i, dict):
                    for k in i:
                        if isinstance(i[k], (int, float)) and i[k] > 50:
                            res += [i]
            return res
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return super().get_stats()


class TransactionStream(DataStream):
    stream_type = "Financial Data"

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            validated_data = [i for i in data_batch if isinstance(i, dict)]
            if self.print_all:
                batch_content = ""
                for i in validated_data:
                    if batch_content != "":
                        batch_content += ", "
                    batch_content += f"{i['type']}:{i['amount']}"
                print(f"Processing Transaction batch: [{batch_content}]")
                net = 0
                for i in validated_data:
                    if i["type"] == "buy":
                        net += i["amount"]
                    else:
                        net -= i["amount"]
                sign = "+" if net >= 0 else ""
                return (f"Transaction analysis: {len(validated_data)} "
                        f"operations, net flow: {sign}{net} units")
            return (f"Transaction data: {len(validated_data)} "
                    "operations processed")
        except Exception:
            return ("Error in TransactionStream processing")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "large":
            res = []
            for i in data_batch:
                if isinstance(i, dict) and "amount" in i and i["amount"] > 100:
                    res += [i]
            return res
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return super().get_stats()


class EventStream(DataStream):
    stream_type = "System Events"

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            validated_data = [i for i in data_batch if isinstance(i, str)]
            if self.print_all:
                batch_content = ""
                for i in validated_data:
                    if batch_content != "":
                        batch_content += ", "
                    batch_content += i
                print(f"Processing event batch: [{batch_content}]")
                error = 0
                for i in validated_data:
                    if i == "error":
                        error += 1
                return (f"Event analysis: {len(validated_data)} events, "
                        f"{error} error detected")
            return f"Event data: {len(validated_data)} events processed"
        except Exception:
            return ("Error in EventStream processing")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "error":
            return [i for i in data_batch
                    if isinstance(i, str) and i == "error"]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return super().get_stats()


class StreamProcessor():
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        if (isinstance(stream, DataStream)):
            self.streams.append(stream)

    def process_streams(self, data: Dict[str, List[Any]]) -> None:
        for stream in self.streams:
            if stream.stream_id in data:
                stream.print_all = False
                res = stream.process_batch(data[stream.stream_id])
                stream.print_all = True
                print(f"- {res}")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    try:
        print("\nInitializing Sensor Stream...")
        sensor = SensorStream("SENSOR_001")
        sensor_info = sensor.get_stats()
        print(f"Stream ID: {sensor_info['stream_id']},",
              f"Type: {sensor_info['stream_type']}")
        sensor_batch = [{"temp": 22.5}, {"humidity": 65}, {"pressure": 1013}]
        print(sensor.process_batch(sensor_batch))
    except Exception as err:
        print(err)

    try:
        print("\nInitializing Transaction Stream...")
        transaction = TransactionStream("TRANS_001")
        transaction_info = transaction.get_stats()
        print(f"Stream ID: {transaction_info['stream_id']},",
              f"Type: {transaction_info['stream_type']}")
        transaction_batch = [
            {"type": "buy", "amount": 100},
            {"type": "sell", "amount": 150},
            {"type": "buy", "amount": 75},
        ]
        print(transaction.process_batch(transaction_batch))
    except Exception as err:
        print(err)

    try:
        print("\nInitializing Event Stream...")
        event = EventStream("EVENT_001")
        event_info = event.get_stats()
        print(f"Stream ID: {event_info['stream_id']},",
              f"Type: {event_info['stream_type']}")
        event_batch = ["login", "error", "logout"]
        print(event.process_batch(event_batch))
    except Exception as err:
        print(err)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    try:
        stream_processor = StreamProcessor()
        stream_processor.add_stream(sensor)
        stream_processor.add_stream(transaction)
        stream_processor.add_stream(event)

        data_batch = {
            "SENSOR_001": [{"temp": 22.5}, {"humidity": 65}],
            "TRANS_001": [
                {"type": "buy", "amount": 100},
                {"type": "sell", "amount": 150},
                {"type": "buy", "amount": 75},
                {"type": "sell", "amount": 100},
            ],
            "EVENT_001": ["login", "error", "logout"]
        }
        print("\nBatch 1 Results:")
        stream_processor.process_streams(data_batch)
    except Exception as err:
        print(err)
    try:
        print("\nStream filtering active: High-priority data only")
        critical_sensors = sensor.filter_data(sensor_batch, "critical")
        large_transaction = transaction.filter_data([
                {"type": "buy", "amount": 100},
                {"type": "sell", "amount": 150},
            ], "large")
        print(f"Filtered results: {len(critical_sensors)} critical sensor "
              f"alerts, {len(large_transaction)} large transaction")
    except Exception as err:
        print(err)
    print("\nAll streams processed successfully. Nexus throughput optimal.")

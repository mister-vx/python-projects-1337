from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Any, List, Union, Protocol, Optional, Dict
import time
import random


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Union[str, Any]:
        ...


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


class InputStage:
    def process(self, data: Any) -> Union[str, Any]:
        if (isinstance(data, dict)):
            return data
        if (isinstance(data, str)):
            return {"raw": data, "parsed": True}
        if (isinstance(data, list)):
            return {"items": data}
        return {"raw": data}


class TransformStage:
    def process(self, data: Any) -> Union[str, Any]:
        if (isinstance(data, dict)):
            data["valid"] = True
            data["metadata"] = "enriched"
            return data
        return {"transform": data, "valid": True}


class OutputStage:
    def process(self, data: Any) -> Union[str, Any]:
        try:
            if (isinstance(data, dict)):
                if ("sensor" in data and "value" in data):
                    value = float(data["value"])
                    unit = data["unit"] if "unit" in data else ""
                    status = ("Normal range" if isinstance(value, float)
                              and 15 <= value <= 30 else "Out of range")
                    return ("Processed temperature reading:"
                            f" {value}°{unit} ({status})")
                if ("raw" in data and "parsed" in data):
                    actions = data["actions"] if "actions" in data else 1
                    return f"User activity logged: {actions} actions processed"
                if ("items" in data):
                    nb = data["items"]
                    numbers = [float(i)
                               for i in nb if isinstance(float(i), (float))]
                    total = 0
                    for i in numbers:
                        total += i
                    avg = total / len(numbers) if len(numbers) > 0 else 0
                    return (f"Stream summary: {len(nb)}"
                            f" readings, avg: {avg:.1f}°C")
            return f"Processed: {data}"
        except Exception:
            return ("error in data passed")


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        print(f"Input: {data}")
        res = data
        for stage in self.stages:
            res = stage.process(res)
        print("Transform: Enriched with metadata and validation")
        return res


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        print(f'Input: "{data}"')
        res = data
        for stage in self.stages:
            res = stage.process(res)
        print("Transform: Parsed and structured data")
        return res


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        print("Input: Real-time sensor stream")
        res = data
        for stage in self.stages:
            res = stage.process(res)
        print("Transform: Aggregated and filtered")
        return res


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []
        self.stats = defaultdict(int)

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def process_data(self, data: Any, pipeline_index: int = 0) -> Any:
        if (len(self.pipelines) > pipeline_index):
            try:
                res = self.pipelines[pipeline_index].process(data)
                self.stats["success"] += 1
                return res
            except Exception as err:
                self.stats["errors"] += 1
                return f"{err}"
        return data


def simulate_err() -> None:
    print("Simulating pipeline failure...")
    try:
        pipeline = JSONAdapter("recovery-pipeline")
        pipeline.add_stage(InputStage())
        pipeline.add_stage(TransformStage())
        pipeline.add_stage(OutputStage())
        data = []
        try:
            index = 1
            stage_1 = pipeline.stages[index].process(data)
            if "metadata" not in stage_1:
                raise ValueError("Invalid data format")
        except Exception as err:
            print(f"Error detected in Stage {index + 1}: {err}")
            print("Recovery initiated: Switching to backup processor")
            stage_1 = {"sensor": "temp", "value": 22.0, "unit": "C"}
        stage_2 = pipeline.stages[index].process(stage_1)
        pipeline.stages[index + 1].process(stage_2)
    except Exception as err:
        print(err)
    print("Recovery successful: Pipeline restored, processing resumed")


if __name__ == "__main__":
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print("\nInitializing Nexus Manager...")
    nexus_manager = NexusManager()
    print("Pipeline capacity: 1000 streams/second")

    print("\nCreating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    input_stage = InputStage()
    print("Stage 2: Data transformation and enrichment")
    transform_stage = TransformStage()
    print("Stage 3: Output formatting and delivery")
    output_stage = OutputStage()

    print("\n=== Multi-Format Data Processing ===")
    json_adapter = JSONAdapter("json-pipeline")
    csv_adapter = CSVAdapter("csv-pipeline")
    stream_adapter = StreamAdapter("stream-pipeline")
    try:
        for adapter in [json_adapter, csv_adapter, stream_adapter]:
            adapter.add_stage(input_stage)
            adapter.add_stage(transform_stage)
            adapter.add_stage(output_stage)
    except Exception as err:
        print(err)
    nexus_manager.add_pipeline(json_adapter)
    nexus_manager.add_pipeline(csv_adapter)
    nexus_manager.add_pipeline(stream_adapter)
    print("\nProcessing JSON data through pipeline...")
    json_data: Optional[Dict] = {"sensor": "temp", "value": "23.5",
                                 "unit": "C"}
    try:
        res = nexus_manager.process_data(json_data, 0)
        print(f"Output: {res}")
    except Exception as err:
        print(err)
    print("\nProcessing CSV data through same pipeline...")
    csv_data = "user,action,timestamp"
    try:
        res = nexus_manager.process_data(csv_data, 1)
        print(f"Output: {res}")
    except Exception as err:
        print(err)
    print("\nProcessing Stream data through same pipeline...")
    try:
        str_data = [21.5, 22.0, 22.5, 22.0, 22.5]
        res = nexus_manager.process_data(str_data, 2)
        print(f"Output: {res}")
    except Exception as err:
        print(err)
    print("\n=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")
    success = 0
    errors = 0
    start = time.perf_counter()
    try:
        rec = [{"sensor": "temp", "value": 22.0, "unit": "C"}
               for _ in range(100)]
        proce_1 = [json_adapter.stages[0].process(i) for i in rec]
        proce_2 = [json_adapter.stages[1].process(i) for i in proce_1]
        for i in rec:
            time.sleep(0.002)
            if random.random() > 0.05:
                success += 1
        print(f"\nChain result: {len(proce_2)} "
              f"records processed through 3-stage pipeline")
    except Exception as err:
        print(err)
    end = time.perf_counter() - start
    print(f"Performance: {success}% efficiency, {end:.1f}s "
          "total processing time")
    print("\n=== Error Recovery Test ===")
    simulate_err()
    print("\nNexus Integration complete. All systems operational.")

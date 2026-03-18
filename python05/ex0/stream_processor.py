from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    print_all = True

    def process(self, data: Any) -> str:
        try:
            if (self.validate(data)):
                if (self.print_all):
                    print("Validation: Numeric data verified")
                if isinstance(data, (int, float)):
                    data = [data]
                t = 0
                for i in data:
                    t += i
                s = len(data)
                avg = t / s if s > 0 else 0
                res = f"Processed {s} numeric values, sum={t}, avg={avg:.1f}"
                if (self.print_all):
                    return self.format_output(res)
                return res
            else:
                raise ValueError("data passed is not numeric")
        except ValueError as err:
            return (f"Validation: {err}")

    def validate(self, data: Any) -> bool:
        try:
            if (isinstance(data, (int, float))):
                return True
            val = 0
            for i in data:
                val += i
            if (data != ""):
                return True
            else:
                return False
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    print_all = True

    def process(self, data: Any) -> str:
        try:
            if (self.validate(data)):
                if self.print_all:
                    print("Validation: Text data verified")

                def count_words(sep: str) -> int:
                    counter = 0
                    sep_in_data = False
                    for i in data:
                        if i != sep:
                            if (not sep_in_data):
                                counter += 1
                                sep_in_data = True
                        else:
                            sep_in_data = False
                    return counter
                s = len(data)
                count = count_words(" ")
                res = f"Processed text: {s} characters, {count} words"
                if self.print_all:
                    return self.format_output(res)
                return res
            else:
                raise ValueError("data passed is not text")
        except Exception as err:
            return (f"Validation: {err}")

    def validate(self, data: Any) -> bool:
        try:
            data + ""
            if (data != ""):
                return True
            else:
                return False
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    print_all = True

    def process(self, data: Any) -> str:
        try:
            if (self.validate(data)):
                j = 0
                found = False
                for i in data:
                    if i == ":":
                        found = True
                        break
                    j += 1
                if (found and len(data[0:j]) > 0):
                    level = data[0:j]
                    val = data[j+1:]
                    if self.print_all:
                        print("Validation: Log entry verified")
                    if (level == "ERROR"):
                        res = f"[ALERT] {level} level detected:{val}"
                        if self.print_all:
                            return self.format_output(res)
                        return res
                    else:
                        res = f"[{level}] {level} level detected:{val}"
                        if self.print_all:
                            return self.format_output(res)
                        return res
                else:
                    raise ValueError("level not found")
            else:
                raise ValueError("data passed is not log string")
        except Exception as err:
            return (f"Validation: {err}")

    def validate(self, data: Any) -> bool:
        try:
            data + ""
            if (data != ""):
                return True
            else:
                return False
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    try:
        num_pro = NumericProcessor()
        text_pro = TextProcessor()
        log_pro = LogProcessor()

        print("\nInitializing Numeric Processor...")
        data = [1, 2, 3, 4, 5]
        print("Processing data:", data)
        res = num_pro.process(data)
        print(res)
    except Exception as err:
        print(err)

    try:
        print("\nInitializing Text Processor...")
        data = "Hello Nexus World"
        print(f'Processing data: "{data}"')
        res = text_pro.process(data)
        print(res)
    except Exception as err:
        print(err)

    try:
        print("\nInitializing Log Processor...")
        data = "ERROR: Connection timeout"
        print(f'Processing data: "{data}"')
        res = log_pro.process(data)
        print(res)
    except Exception as err:
        print(err)

    print("\n=== Polymorphic Processing Demo ===")

    try:
        print("Processing multiple data types through same interface...")
        lst = [num_pro, text_pro, log_pro]
        data = [[1, 2, 3], "Hello Nexus ", "INFO: System ready"]
        j = 0
        for i in lst:
            i.print_all = False
            res = i.process(data[j])
            print(f"Result {j + 1}:", res)
            j += 1
    except Exception as err:
        print(err)
    print("\nFoundation systems online. Nexus ready for advanced streams.")

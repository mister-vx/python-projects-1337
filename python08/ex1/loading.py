import importlib


def compare_versions(pkg: str, version: str, desc: str) -> None:
    packages = [
        {"package": "pandas", "version": "2.1.0"},
        {"package": "numpy", "version": "1.25.0"},
        {"package": "matplotlib", "version": "3.7.2"},
    ]
    for i in packages:
        if (i["package"] == pkg):
            if version == i["version"]:
                print(f"[OK] {pkg} ({version}) - {desc} ready")
            else:
                print(f"[OK] {pkg} ({version}) "
                      f"recommended ({i['version']}) - {desc} ready")


def is_packages_installed() -> bool:
    packages = {
        "pandas": "Data manipulation",
        "numpy": "Numerical computation",
        "matplotlib": "Visualization"
    }
    print("Checking dependencies:")
    installed = True
    for package, desc in packages.items():
        try:
            module = importlib.import_module(package)
            version = module.__version__
            compare_versions(package, version, desc)
        except ImportError:
            print(f"[MISSING] {package} - {desc}")
            installed = False
    if not installed:
        print("\nInstall missing packages:")
        print(" with pip: pip install -r requirements.txt")
        print(" with Poetry: poetry install")
    return installed


if __name__ == "__main__":
    try:
        print("\nLOADING STATUS: Loading programs...\n")
        if is_packages_installed():
            pandas = importlib.import_module("pandas")
            numpy = importlib.import_module("numpy")
            p = importlib.import_module("matplotlib.pyplot")
            nb = 1000
            print("\nAnalyzing Matrix data...")
            print(f"Processing {nb} data points...")
            data = numpy.random.randn(nb)
            data_frame = pandas.DataFrame(data, columns=["values"])
            status_analyze = data_frame.describe()
            mean_v = status_analyze.loc["mean", "values"]
            max_v = status_analyze.loc["max", "values"]
            min_v = status_analyze.loc["min", "values"]
            image = "matrix_analysis.png"
            print("Generating visualization...\n")
            p.hist(data, bins=40, color="skyblue", edgecolor="black")
            p.title("Matrix Data Distribution\n"
                    f"mean={mean_v:.2f}, max={max_v:.2f}, min={min_v:.2f}")
            p.xlabel("Value")
            p.ylabel("Frequency")
            p.savefig(image)
            p.close()
            print("Analysis complete!")
            print(f"Results saved to: {image}")
    except Exception as err:
        print(err)

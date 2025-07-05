import multiprocessing
import subprocess

def run_prediction_api():
    subprocess.run(["python", "backend/assessment.py"])

if __name__ == "__main__":
    api = multiprocessing.Process(target=run_prediction_api)

    api.start()
    api.join()
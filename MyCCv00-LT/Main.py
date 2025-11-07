if __name__ == "__main__" only in main.py

from config import DEFAULT_LANGUAGE, OUTPUT_DIR
from content import generate_caption, summarize_section
from io_utils import write_svg, read_prn
from visualizer import create_seesaw_chart
from launcher import build_restart_safe_cmd
from legacy_safe import safe_run
from utils import log, version_info

def main():
    log("Starting CCED publishing pipeline")
    safe_run(lambda: generate_caption("input.md"))
    safe_run(lambda: create_seesaw_chart("data.csv"))
    build_restart_safe_cmd("launch_typst.bat")

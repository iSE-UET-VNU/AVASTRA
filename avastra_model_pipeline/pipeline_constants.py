APOLLO_HOST = "112.137.129.158"
DREAMVIEW_PORT = 9988
EXTRACTOR_PORT = 8966

SIMULATOR_HOST = "localhost"
SIMULATOR_PORT = 8977

API_SERVER_HOST = "localhost"
API_SERVER_PORT = 8933

SANFRANCISCO_MAP = '12da60a7-2fc9-474d-a62a-5cc08cb97fe8'
TARTU_MAP = 'bd77ac3b-fbc3-41c3-a806-25915c777022'
BORREGAS_AVE_MAP = 'aae03d2a-b7ca-4a88-9e41-9035287a12cc'

NUMBER_WEATHER_TIME = 13
NUMBER_NPC_VEHICLE = 30
NUMBER_PEDESTRIAN = 2

USE_WEATHER_TIME = True
USE_NPC_VEHICLE = True
USE_PEDESTRIAN = True

HyperParameter = dict(BATCH_SIZE=64, GAMMA=0.9, EPS_START=1, EPS_END=0.1, EPS_DECAY=8500, TARGET_UPDATE=100,
                      lr=1e-3 * 3, INITIAL_MEMORY=3000, MEMORY_SIZE=3000, WEIGHT_DECAY=1e-5, LEARNING_RATE_DECAY=0.8, 
                      NUM_LAYER_1=1024, NUM_LAYER_2=512, PARAM_INIT_RANGE=0.01, PER_EPS=0.01, PER_ALPHA=0.7, PER_BETA=0.4)

PROB_DECAY = 0.05
OBSERVATION_TIME = 6
STOP_STEP = 5
ROAD_NUM = "2"

STOP_DIS = 3
STOP_DIS_ALTITUDE = 25

RCOL = 7.5
PENALTY_THRESHOLD = 0.2
PENALTY = -1

MODEL_PATH = "model"
LOG_PATH = "ExperimentData/Log"
IN_MODEL_NAME = 'avastra_standard_sanfrancisco_road3'
OUT_MODEL_NAME = 'avastra_standard_sanfrancisco_road3'
LOG_NAME = 'avastra_standard_sanfrancisco_road3'
REUSE_MEMORY_NAME = ""

TEST_PATH = "ExperimentData/Test"
TEST_NAME = 'avastra_standard_sanfrancisco_road3'
TEST_ATTEMPT = 5
TEST_SCENARIO_NUM = 15
TEST_MODEL_EPS = 5

RANDOM_SEARCH_NAME = 'random_search_sanfrancisco_road3'
CC = clang
CFLAGS = -Wall -Wextra -g -O3 -Iinclude
SRC_DIR = src
BIN_DIR = bin
SHARED_DIR = src/shared

# Find shared logic and algorithm files
SHARED_SRCS = $(wildcard $(SHARED_DIR)/*.c)
SHARED_OBJS = $(patsubst $(SHARED_DIR)/%.c, $(BIN_DIR)/shared/%.o, $(SHARED_SRCS))
ALGO_SRCS = $(filter-out $(SHARED_SRCS), $(wildcard $(SRC_DIR)/*/*.c) $(wildcard $(SRC_DIR)/*.c))
BINS = $(patsubst $(SRC_DIR)/%.c, $(BIN_DIR)/%, $(ALGO_SRCS))

.PHONY: all clean directories

all: directories $(BINS)

directories:
	@mkdir -p $(BIN_DIR)/shared
	@mkdir -p $(dir $(BINS))

$(BIN_DIR)/shared/%.o: $(SHARED_DIR)/%.c
	$(CC) $(CFLAGS) -c $< -o $@

$(BIN_DIR)/%: $(SRC_DIR)/%.c $(SHARED_OBJS)
	$(CC) $(CFLAGS) $< $(SHARED_OBJS) -o $@

clean:
	rm -rf $(BIN_DIR)
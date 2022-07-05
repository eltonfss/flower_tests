import flwr as fl

# Start Flower server
fl.server.start_server(
  "[::]:8081",
  config={"num_rounds": 3},
)

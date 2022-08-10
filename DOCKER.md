# Blog

## Init Application
```shell
make init
```

#### ... step by step:
1. `make compose.build`
2. `make compose.up`


## Test
Run test:

```shell
make test
```

## Cleanup
Remove docker-compose stack:
```shell
make compose.down
```

## Others
Some additional commands:
- `make compose.build.nocache` (re)build container without cached layers
- `make compose.restart` take down, (re)build, and take up docker containers

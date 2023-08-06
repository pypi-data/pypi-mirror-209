# Timey-wimey
A simple CLI tool to generate dates from plain English. 

## Usage

You can pass in a string using natural language and it'll parse it.
```shell
❯ timey-wimey "two hours ago utc"
2023-05-19T00:13:27.866775+00:00
```

If you want a range of dates you can use the `--to` flag to get it. You use the `--interval` flag to set the 
interval it increments by. The interval should be in the format: `integer unit` so like: `3 days` or `1 hour`.

```shell
❯ timey-wimey "two hours ago utc" --to "three hours utc" --interval "30 minutes"         
2023-05-19T00:15:30.469480+00:00
2023-05-19T00:15:30.469480+00:00
2023-05-18T23:45:30.469480+00:00
```


## Instal

```shell
pipx install timey-wimey
```
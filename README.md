# Litestar Emit Exception Failure Example

This quick app was created to show an issue that happens when an exception occurs inside an event
listener. When an exception is raised inside the listener, the listener stream is closed and no
additional events are able to be picked up.

## Run it

```
pipenv install
litestar run -d
```

- Go to `http://localhost:8000/check-value/2` to see a successful request
- Go to `http://localhost:8000/check-value/3` to see an exception raised in the listener
- Attempt to go to `http://localhost:8000/check-value/2` again, but you should get
    `ClosedResourceError`

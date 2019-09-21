workflow "CI" {
  on = "push"
  resolves = [
    "foo",
  ]
}

action "foo" {
  uses = "docker://alpine"
  runs = "echo foo ; exit 0"
}

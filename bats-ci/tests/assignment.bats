#!/usr/bin/env bats

@test "assignment" {
  result="$(echo foo)"
  [ "$result" == "foo" ]
}

#!/usr/bin/env bats

@test "assignment" {
  result="$(echo foo)"
  [ "$result" == "foo" ]
}

@test "assignment 2" {
  result="$(echo foo)"
  [ "$result" == "foo2" ]
}

# @test "addition using bc" {
#   result="$(echo 2+2 | bc)"
#   [ "$result" -eq 4 ]
# }

# @test "addition using dc" {
#   result="$(echo 2 2+p | dc)"
#   [ "$result" -eq 4 ]
# }

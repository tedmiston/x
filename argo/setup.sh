#!/usr/bin/env bash

set -euxo pipefail

sudo curl -sfL https://get.k3s.io | sh -
sudo systemctl status k3s
sudo k3s kubectl --version
sudo systemctl stop k3s
echo "running k3s command"
sudo k3s server --docker --disable-agent &
sudo k3s kubectl get nodes
sudo kubectl get nodes
sudo k3s kubectl get pods --all-namespaces
sudo kubectl get pods --all-namespaces

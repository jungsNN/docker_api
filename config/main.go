package main

import (
    "io/ioutil"
    "github.com/jungsnn/docker_api/config/domain"


)


func main() {
    config := domain.Config{}

    data, err := ioutil.ReadFile("config.yaml")
    if err != nil {
        panic(err)
    }

    err = config.SetFromBytes(data)
    if err != nil {
        panic(err)
    }

    fmt.Println(config.Get("service.registry.state"))
}
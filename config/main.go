package main

import (
    "log"
    "time"

    "github.com/jungsnn/muxinator"

    "github.com/jungsnn/docker_api/config/controller"
    "github.com/jungsnn/docker_api/config/domain"
    "github.com/jungsnn/docker_api/config/service"

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

    fmt.Println(config.Get("service.registry.state")
}
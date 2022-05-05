[![CircleCI](https://circleci.com/gh/svk100/Capstone-Udacity.svg?style=svg)](https://circleci.com/gh/svk100/Capstone-Udacity/tree/main)

## Project Overview
<h1 >Cloud DevOps Engineer Nanodegree by Udacity: Capstone Project</h1>

In this project you will apply the skills and knowledge which were developed throughout the Cloud DevOps Nanodegree program. These include:

* Working in AWS
* Using Jenkins or Circle CI to implement Continuous Integration and Continuous Deployment
* Building pipelines
* Working with Ansible and CloudFormation to deploy clusters
* Building Kubernetes clusters
* Building Docker containers in pipelines

## Overview: 
	- I'm deploying a dockerized python app, called greenapp to a AWS EKS Cluster.
	- I'll be using Cloudformation, circleci, docker hub, Amazon EKS
	- I'll be updating the docker image to blueapp using rolling deployment
	- I've highlighted the loadbalancer url in the screenshots to show the same cluster getting updated to a new image
	   Screenshots <a href="doc:Screenshots/4.3 LoadBalancer_Created.JPG" target="_blank">4.3</a> , 5.3 and 7.3

## Requirements

* Develop a CI/CD pipeline for micro services applications with either blue/green deployment or rolling deployment
	1. My microservices application is hosted in AWS Elastic Kubernetes Service
	2. I've used circleci for CI/CD
	3. I've implemented a rolling deployment
	
* Develop your Continuous Integration steps as you see fit, but must at least include typographical checking (aka “linting”)
	1. My Pipiline includes
		- Docker Build
		- Linting
		- Deployment to EKS Cluster
		- Smoke test

* Set up Continuous Deployment, which will include:
	1. Pushing the built Docker container(s) to the Docker repository
		- I've published my Docker images to Docker Hub
	2. Deploying these Docker container(s) to a small Kubernetes cluster
		- I've deployed my docker containers to EKS
		- I've demonstrated a rolling deployment, where I changed the docker image and also scaled the cluster from 2 to 4 nodes
	3. Deploy your Kubernetes cluster, use either Ansible or Cloudformation. Preferably, run these from within Jenkins or Circle CI as an independent pipeline.
		- I've deployed using Cloudformation
		- I've used circleci to run the Cloudformation scripts
		- I've used the same pipeline, but my pipeline is parameterized and well modularized.


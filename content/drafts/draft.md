Now, let's run a pod.
First create a manifest file. `pod.yml`
```yaml
apiVersion: v1  # depends on version of k8s we are using
kind: Pod  # it's obvious that its a pod
metadata:
  name: hello-pod  # this is the name of our pod
spec:  # define specifications for our pod
  containers:
    - name: hello-ctr  # container name
      image: nigelpoulton/pluralsight-docker-ci:latest  # image name
      ports:
        - containerPort: 8000  # port inside the container
```

Run the pod:
```bash
$ kubectl create -f pod.yml
```

Get pod description:
```bash
$ kubectl describe pods
```

.PHONY: image sample

image:
	docker build -t manim-japanese .

sample:
	docker run --rm -it --user="$(id -u):$(id -g)" -v ./manim:/manim manim-japanese manim sample.py Sample -qm
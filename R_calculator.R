##This is a calculator program
##Izabela Tyrna 10358601

#Calcualtor

variable <- ''

add_func <- function(x, y) {
  return(x + y)
}

subtract_func <- function(x, y) {
  return(x - y)
}

multiply_func <- function(x, y) {
  return(x * y)
}

divide_func <- function(x, y) {
  ifelse(y != 0,return(x / y),"Do not divide by 0")
}

square_func <- function(x) {
  return(x^2)
}

squareroot_func <- function(x) {
  return(sqrt(x))
}

cube_func <- function(x) {
  return(x*x*x)
}

power_func <- function(x,y) {
  return(x^y)
}

factorial_func <- function(x) {
  return(factorial(x))
}

sin_func <- function(x) {
  return(sin(x))
}


#calling calcualtor functions
add_func(1,1)
subtract_func(1,1)
multiply_func(1,2)
divide_func(1,2)
divide_func(2,0)
divide_func(2,0.5)
square_func(4)
squareroot_func(4)
cube_func(2.0)
power_func(2,3)
power_func(2,-3)
factorial_func(3)
sin_func(2)
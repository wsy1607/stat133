student <- function(name,age,sex){
  object <- list(name = name, age = age, sex= sex)
  class(object) <- "student"
  return(object)
}
display.student <- function(object){
  cat(sprintf('%s is a %s student with age %d',object$name,object$sex,object$age))
}
Bob <- student(name='Bob',age=20,sex='M')
display(Bob)
print(Bob)
.data
	message: .asciiz "Different"
	message1: .asciiz "Same"
.text
	main:
		addi $t0, $zero, 5
		addi $t1, $zero, 20
	
		beq $t0, $t1, numbersSame
		
		bne $t0, $t1, numbersDifferent
			
		li $v0, 10
		syscall
	
	numbersDifferent:
		li $v0, 4
		la $a0, message
		syscall
		
		li $v0, 10
		syscall
		
	numbersSame:
		li $v0, 4
		la $a0, message1
		syscall
	

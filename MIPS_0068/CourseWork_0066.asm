.data
	welcomeMessage: .asciiz "This program implements the equation E = Z*5/3 + 7 \n \n"
	enter: .asciiz "Enter an integer Z: "
	right: .asciiz "\nRight side."
	left: .asciiz "\nLeft side."
	ee: .asciiz "\nE = "
.text
	main:		# CHANGE $T INTO $A AND $S INTO $T EXCEPT FOR THE LAST RESULT WHICH SHOULD BE $S (note 100% but should be like that)
		li $v0, 4
		la $a0, welcomeMessage
		syscall
		
		li $v0, 4
		la $a0, enter
		syscall
		
		li $v0, 5
		syscall
		move $s0, $v0
		
		jal equation # puts this function into the $ra address AND jumps down to where the function is defined
		jal check
		
		beq $t3, $zero, printLeft
		bne $t3, $zero, printRight
		
	li $v0, 10
	syscall
		
	equation:
		addi $s1, $zero, 5
		addi $s2, $zero, 3
		addi $s3, $zero, 7
		
		mul $t0, $s0, $s1
		div $t1, $t0, $s2
		add $t2, $t1, $s3
		
		li $v0, 4
		la $a0, ee
		syscall
		
		li $v0, 1
		add $a0, $zero, $t2 # E is stored in $t2
		syscall
		
		jr $ra		    # jumps to address corrsponding to previous jal command
		
		li $v0, 10
		syscall
		
	check:
		slt $s4, $t2, $s3
		jr $ra
		
		li $v0, 10
		syscall
		
	printLeft:
		li $v0, 4
		la $a0, left
		syscall
		
		li $v0, 10
		syscall
		
	printRight:
		li $v0, 4
		la $a0, right
		syscall
		
		li $v0, 10
		syscall
		
		
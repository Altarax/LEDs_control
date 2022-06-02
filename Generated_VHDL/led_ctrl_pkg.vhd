
--! \file led_matrix_ctrl_pkg.vhd
--!
--! \brief Package to control leds matrix.
--!
--! \version 1.0
--! \date 2022-05-31
--!
--! \author Jayson Dangremont, dangremontjayson.pro@gmail.com

library IEEE;
use IEEE.STD_LOGIC_1164.all;

package led_ctrl_package is

	--! Custom types
	type LED_matrix_type is array (0 to 255) of std_logic_vector(23 downto 0);
	
	--! Main variable created by python file
	constant LED : LED_matrix_type := (
        			X"1DED24", X"1DED24", X"1DED24", X"1DED24", X"1DED24", X"1DED24", X"1DED24", X"1DED24", X"FEFFFE", X"FEFFFE", 
			X"FEFFFE", X"FEFFFE", X"FEFFFE", X"FEFFFE", X"FEFFFE", X"1DED24", X"1DED24", X"FFFFFF", X"FFFFFF", X"FFFFFF", 
			X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"1DED24", X"1DED24", X"1DED24", X"FFFFFF", X"FFFFFF", X"FFFFFF", 
			X"FFFFFF", X"1DED24", X"1DED24", X"1DED24", X"1DED24", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", 
			X"1DED24", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"1DED24", X"1DED24", X"1DED24", X"FFFFFF", 
			X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", 
			X"FFFFFF", X"FFFFFF", X"FFFFFF", X"1DED24", X"1DED24", X"1DED24", X"1DED24", X"1DED24", X"1DED24", X"1DED24", 
			X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"1DED24", X"1DED24", 
			X"1DED24", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"9BF79E", X"FFFFFF", X"1DED24", X"1DED24", X"FFFFFF", 
			X"40F045", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"1DED24", X"1DED24", X"1DED24", X"FFFFFF", X"FFFFFF", 
			X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"1DED24", X"1DED24", X"1DED24", X"1DED24", 
			X"1DED24", X"1DED24", X"1DED24", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", 
			X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"1DED24", X"1DED24", X"FFFFFF", 
			X"FFFFFF", X"1DED24", X"FFFFFF", X"FFFFFF", X"F9FFF9", X"1DED24", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", 
			X"FFFFFF", X"FFFFFF", X"FFFFFF", X"1DED24", X"1DED24", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"1DED24", 
			X"1DED24", X"FFFFFF", X"1DED24", X"1DED24", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"1DED24", 
			X"1DED24", X"1DED24", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", 
			X"FFFFFF", X"FFFFFF", X"1DED24", X"1DED24", X"1DED24", X"1DED24", X"1DED24", X"FFFFFF", X"FFFFFF", X"FFFFFF", 
			X"FFFFFF", X"FFFFFF", X"FFFFFF", X"1DED24", X"1DED24", X"1DED24", X"1DED24", X"1DED24", X"1DED24", X"FFFFFF", 
			X"FFFFFF", X"1DED24", X"1DED24", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", 
			X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"1DED24", X"1DED24", X"FFFFFF", 
			X"1DED24", X"1DED24", X"FFFFFF", X"1DED24", X"1DED24", X"FFFFFF", X"FFFFFF", X"1DED24", X"1DED24", X"FFFFFF", 
			X"1DED24", X"1DED24", X"FFFFFF", X"1DED24", X"1DED24", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", 
			X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"FFFFFF", X"1DED24", 
			X"1DED24", X"1DED24", X"1DED24", X"1DED24", X"1DED24", X"1DED24", X"1DED24", X"FFFFFF", X"FFFFFF", X"1DED24", 
			X"1DED24", X"1DED24", X"1DED24", X"1DED24", X"1DED24", X"1DED24");
	
	--! Functions declarations
	function reset_matrix(matrix : in LED_matrix_type) return LED_matrix_type;
	
end package led_ctrl_package;

package body led_ctrl_package is

	-- Functions implementations
	function reset_matrix(matrix : in LED_matrix_type) return LED_matrix_type is
		variable temp_matrix : LED_matrix_type := matrix;
	begin
		for i in 0 to (matrix'length-1) loop
			temp_matrix(i) := x"000000";
		end loop;
		return temp_matrix;
	end function;

end package body led_ctrl_package;
    
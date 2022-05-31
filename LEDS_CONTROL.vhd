--! \file LEDS_CONTROL.vhd
--!
--! \brief Main file to create LEDS control.
--!
--! \version 1.0
--! \date 2021-12-04
--!
--! \author ('Jayson Dangremont', 'dangremontjayson.pro@gmail.com')

--! Use standard library.
library IEEE;

--! Use logic elements library.
use IEEE.STD_LOGIC_1164.ALL;

--! Use numeric elements library
use IEEE.NUMERIC_STD.ALL;

--! Use custom library
library work;
use work.led_ctrl_package.all;

entity LEDS_CONTROL is
    Port (
    
        clk         	: in std_logic; 
		  reset			: in std_logic;

        sent_data   	: out std_logic
                
    );
end LEDS_CONTROL;

architecture arch of LEDS_CONTROL is

	constant T0H : integer := 17;
	constant T0L : integer := 38;
	constant T1H : integer := 35;
	constant T1L : integer := 28;
	constant RES : integer := 2500;

	--! State machine types
	xtype state_machine is (load, sending, send_bit, reset_state);

   	--! Internal signal copied on output
   	signal sent_data_s  : std_logic;
	signal LED_v : LED_matrix_type := LED;

begin

	LEDS_gen: process(clk)
		variable state : state_machine := load;
		variable GRB : std_logic_vector(23 downto 0) := x"000000";
		variable delay_high_counter : integer := 0;
		variable delay_low_counter : integer := 0;
		variable index : integer := 0;
		variable bit_counter : integer := 0;

	begin
				
		if rising_edge(clk) then

			case state is

				when load =>
				
							GRB := LED_v(index);
							bit_counter := 24;
							state := sending;

				when sending =>
				
						if (bit_counter > 0) then
							bit_counter := bit_counter - 1;
							if GRB(bit_counter) = '1' then
								delay_high_counter := T1H;
								delay_low_counter := T1L;
							else
								delay_high_counter := T0H;
								delay_low_counter := T0L;
							end if;
								state := send_bit;
						else
							if (index < LED_matrix_type'length) then
								index := index + 1;
								state := load;
							else
								delay_low_counter := RES;
								state := reset_state;
							end if;
						end if;
							  
				when send_bit =>
				
						if (delay_high_counter > 0) then
							sent_data <= '1';
							delay_high_counter := delay_high_counter - 1;
						elsif (delay_low_counter > 0) then
								sent_data <= '0';
								delay_low_counter := delay_low_counter - 1;
						else
							state := sending;
						end if;

				when reset_state =>
				
						if (delay_low_counter > 0) then
							sent_data <= '0';
							delay_low_counter := delay_low_counter - 1;
						else
							index := 0;
						end if;

				when others => null;

			end case;
		end if;
		
	end process;

end arch;
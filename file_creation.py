# Imports
from datetime import date

# Global variables
FILE    = "LEDS_CONTROL.vhd"
AUTHOR  = "Jayson Dangremont"
MAIL    = "dangremontjayson.pro@gmail.com"
VERSION = "1.0"
BRIEF   = "Main file to create a leds control file in VHDL"
DATE    = date.today()

MIN_RESET_CODE  = 50    # us
FREQ_CLOCK      = 50    # Mhz
NB_OF_LEDS      = 256   # int

def create_main_vhd(data_led_matrix):
    file = open(FILE, 'w')

    file.write(f'''--! \\file {FILE}
--!
--! \\brief Main file to create LEDS control.
--!
--! \\version {VERSION}
--! \\date {DATE}
--!
--! \\author {AUTHOR, MAIL}

--! Use standard library.
library IEEE;

--! Use logic elements library.
use IEEE.STD_LOGIC_1164.ALL;

--! Use numeric elements library
use IEEE.NUMERIC_STD.ALL;

entity LEDS_CONTROL is
    Port (
    
        clk         : in std_logic; 

        sent_data   : out std_logic
                
    );
end LEDS_CONTROL;

architecture arch of LEDS_CONTROL is

	constant T0H : integer := 17;
	constant T0L : integer := 38;
	constant T1H : integer := 35;
	constant T1L : integer := 28;
	constant RES : integer := 2500;

    type LED_matrix is array (0 to {NB_OF_LEDS-1}) of std_logic_vector(23 downto 0);
	type state_machine is (load, sending, send_bit, reset);

    --! Internal signal copied on output
    signal sent_data_s  : std_logic;

begin

    --! Connect internal signal to output
    sent_data <= sent_data_s;

	LEDS_gen: process
		variable state : state_machine := load;
		variable GRB : std_logic_vector(23 downto 0) := x"000000";
		variable delay_high_counter : integer := 0;
		variable delay_low_counter : integer := 0;
		variable index : integer := 0;
		variable bit_counter : integer := 0;
		variable LED : LED_matrix := (--! generate each pixel
            {data_led_matrix}
        );

	begin
		wait until rising_edge(clk);
	
		case state is

			when load =>
						GRB := LED(index);
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
						if (index < 15) then
							index := index + 1;
							state := load;
						else
							delay_low_counter := RES;
							state := reset;
						end if;
					end if;
                    
			when send_bit =>
					if (delay_high_counter > 0) then
						sent_data_s <= '1';
						delay_high_counter := delay_high_counter - 1;
					elsif (delay_low_counter > 0) then
						sent_data_s <= '0';
						delay_low_counter := delay_low_counter - 1;
					else
						state := sending;
					end if;

			when reset =>
					if (delay_low_counter > 0) then
						sent_data_s <= '0';
						delay_low_counter := delay_low_counter - 1;
					else
						index := 0;
					end if;

			when others => null;

		end case;

	end process;

end arch;

    ''')

    file.close()
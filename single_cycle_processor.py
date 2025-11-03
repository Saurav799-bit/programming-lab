from .processor import Processor
from .riscv_tables import *

class SingleCycleProcessor(Processor):
    def __init__(self, start, ram, logger, st):
        super().__init__(start, ram, logger)
        self.stats = st

    def run(self, num_insts):
        """
        Run the processor in a single cycle for each instruction.
        """
        i_cnt = 0
        pc = self.pc
        self.logr.info("Started single cycle processor")
        
        while i_cnt < num_insts:
            self.logr.info(f"[DEBUG] Fetching instruction at PC = {hex(pc)}")

            # Instruction fetch 
            instruction, next_pc = self.fetch(pc, self.mem)
            if instruction is None:
                self.logr.info(f"[DEBUG] No instruction found at {hex(pc)} - stopping simulation.")
                break

            # Instruction decode 
            op, decoded = self.decode(instruction)
            if decoded is None:
                self.logr.info(f"[DEBUG] Decode failed for instruction {hex(instruction)} - stopping.")
                break
            self.logr.info(f"[DEBUG] Decoded = {decoded}")

            # Operand fetch 
            op1, op2 = self.operand_fetch(decoded, self.registers, pc)
            op = decoded.get("op", None)
            
            # Execute 
            result = self.execute(op, op1, op2)
            self.logr.debug(f"Execute result: op1={op1:08x}, op2={op2 if isinstance(op2, int) else 0:08x}, result={result:08x}")
            
            # Memory access 
            ldata = self.mem_access(op, result, self.mem, self.registers, decoded)
            
            # Update PC
            new_pc = self.update_pc(pc, op, result, decoded, self.registers)

            # Register write back 
            self.registers = self.reg_write(op, decoded, result, ldata,
                                            self.registers, pc, new_pc,
                                            self.mem, self.logr)

            # Update statistics and increment counters
            self.stats.increment_instruction_count()
            i_cnt += 1
            pc = new_pc

        self.pc = pc
        self.logr.info(f"Simulation complete: executed {i_cnt} instructions.")
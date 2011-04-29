# --------------------------------------------------
# Convenience Methods
# --------------------------------------------------
def all_rspec_files
  Dir['rspec/*.spec']
end


# --------------------------------------------------
# Handling of execution
# --------------------------------------------------
def run_all_files
  run_all_rspecs
  puts
  run_all_qunits
  no_int_for_you
end

def run_internal(command, files)
  puts "files to run: #{files}"
  system "#{command} #{files}"
end

def run_all_rspecs
  run_internal("rspec -c -fd", all_rspec_files.join(' '))
end

def run_all_qunits
  run_internal("echo", "not implemented yet")
end

# --------------------------------------------------
# Watchr Rules
# --------------------------------------------------
watch('^rspec/(.*)\.spec')       { run_all_rspecs }
watch('^rspec/spec_helper\.rb')  { run_all_files }
watch('^lib/(.*)\.rb')           { run_all_files }
watch('^views/(.*)\.haml')       { run_all_files }
#watch('^*.rb')                   { run_all_files }

# --------------------------------------------------
# Signal Handling
# --------------------------------------------------

def no_int_for_you
  @sent_an_int = nil
end

Signal.trap 'INT' do
  if @sent_an_int then
    puts "   A second INT?  Ok, I get the message.  Shutting down now."
    exit
  else
    puts "   Did you just send me an INT? Ugh.  I'll quit for real if you do it again."
    @sent_an_int = true
    Kernel.sleep 0.5
    run_all_files
  end
end
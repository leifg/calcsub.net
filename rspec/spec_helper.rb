require File.join(File.dirname(__FILE__), '..', 'lib','ip_range.rb')
require File.join(File.dirname(__FILE__), '..', 'lib','frontend_helper.rb')
require File.join(File.dirname(__FILE__), '..', 'calc.rb')
require File.join(File.dirname(__FILE__), '..', 'lib','options.rb')

require 'rubygems'
require 'sinatra'
require 'rack/test'
require 'rspec'

# set test environment
set :environment, :test
set :run, false
set :raise_errors, true
set :logging, false
require File.join(File.dirname(__FILE__), '..', 'lib','ip_range_metadata.rb')

require 'rubygems'
require 'sinatra'
require 'rack/test'
require 'rspec'

# set test environment
set :environment, :test
set :run, false
set :raise_errors, true
set :logging, false
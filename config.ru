require 'rubygems'
require 'sinatra'
require 'sinatra/reloader'
require "./calc.rb"

enable :logging
set :environment, :production
set :jquery_version, '1.5.2'
set :port, 4567
run Sinatra::Application
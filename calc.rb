require 'sinatra'
require 'haml'
require 'sass'
require File.join(File.dirname(__FILE__),'lib','ip_range.rb')
require File.join(File.dirname(__FILE__),'lib','format_helper.rb')

get '/css/style.css' do
  headers \
   'Content-Type' => 'text/css; charset=utf-8'
  sass :style
end

get '/' do
  "empty"
end

get '/:address/:prefix' do
  @data = IpRange.new(params[:address],params[:prefix])
  @format_hash = FrontendFormatHelper.new(@data).dotted_hash
  
  haml :ip
end
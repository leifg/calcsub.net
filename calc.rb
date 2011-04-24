require 'sinatra'
require 'haml'
require 'sass'
require File.join(File.dirname(__FILE__),'lib','ip_range.rb')
require File.join(File.dirname(__FILE__),'lib','frontend_helper.rb')

@@default_address = '192.168.0.1'
@@default_prefix = 24

get '/css/style.css' do
  headers \
   'Content-Type' => 'text/css; charset=utf-8'
  sass :style
end

post '/post' do
  redirect "/#{params[:address_with_prefix]}"
end

get '/' do
  redirect "#{@@default_address}/#{@@default_prefix}"
end

# get '/:any_string' do
#   @data=IpRange.new(nil)
#   @string_for_input = params[:any_string]
#   @frontend_helper = FrontendHelper.new(@data)
#   haml :ip
# end

get '/:address/:prefix' do
  @data = IpRange.new(params[:address],params[:prefix])
  if @data.valid?
    @string_for_input = "#{@data.address}/#{@data.prefix.to_s }"
  else
    @string_for_input = "#{params[:address]}/#{params[:prefix]}"
  end
  @frontend_helper = FrontendHelper.new(@data)
  haml :ip
end
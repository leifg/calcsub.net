require 'sinatra'
require 'haml'
require File.join(File.dirname(__FILE__),'lib','ip_range_metadata.rb')

get '/:address/:prefix' do
  ip_address = params[:address]
  prefix = params[:prefix]
  
  "address entered: #{params[:address]}\n mask length: #{params[:prefix]}"
  
  @data = IpRangeMetadata.new(ip_address,prefix)
  haml :ip
end
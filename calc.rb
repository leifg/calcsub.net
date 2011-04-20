require 'sinatra'

get '/:address/:mask_length' do
  "address entered: #{params[:address]}\n mask length: #{params[:mask_length]}"
end
require File.join(File.dirname(__FILE__),'ip_range.rb')

class FrontendHelper

  @@Invalid_input_string = "invalid input"
  @IP_Range

  def initialize(ip_range)
    @IP_Range = ip_range
  end
  
  def html_formated_address
    hash = @IP_Range.dotted_hash rescue nil
    
    if hash
      "<span class='net_style' id='net'>#{hash[:net]}</span><span class='mixed_style' id='mixed'>#{hash[:mixed]}</span><span class='host_style' id='host'>#{hash[:host]}</span>"
    else
      "<span class='address_error_style' id='address_error'>#{@@Invalid_input_string}</span>"
    end
  end
end
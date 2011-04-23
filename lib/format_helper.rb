require File.join(File.dirname(__FILE__),'ip_range.rb')

class FrontendFormatHelper

  @IP_Range

  def initialize(ip_range)
    @IP_Range = ip_range
  end

  def dotted_hash
    
    hash = @IP_Range.split
    net_string = hash[:net].join(@IP_Range.separator)+"." unless hash[:net].length == 0
    mixed_string = hash[:mixed].join(@IP_Range.separator)+"." unless hash[:mixed].length == 0
    host_string = hash[:host].join(@IP_Range.separator) unless hash[:host].length == 0
    
    if host_string.nil?
      if mixed_string.nil?
        net_string.chomp!(@IP_Range.separator)
      else
        mixed_string.chomp!(@IP_Range.separator)
      end
    end
    
    {:net => net_string, :mixed => mixed_string, :host => host_string}
  end
end
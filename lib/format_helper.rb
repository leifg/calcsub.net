require File.join(File.dirname(__FILE__),'ip_range.rb')

class FrontendFormatHelper

  @IP_Range

  def initialize(ip_range)
    @IP_Range = ip_range
  end

  def dotted_hash
    
    hash = @IP_Range.split
    net_string = hash[:net].join(@IP_Range.separator)+@IP_Range.separator unless hash[:net].length == 0
    mixed_string = hash[:mixed].join(@IP_Range.separator)+@IP_Range.separator unless hash[:mixed].length == 0
    host_string = hash[:host].join(@IP_Range.separator) unless hash[:host].length == 0
    
    remove_separators(net_string, mixed_string, host_string)
    
    {:net => net_string, :mixed => mixed_string, :host => host_string}
  end
  
  private
  def remove_separators(net_string, mixed_string, host_string)
    if (to_remove?(net_string, mixed_string, host_string))
      net_string.chomp!(@IP_Range.separator)
    end
    
    if (to_remove?(mixed_string, host_string))
      mixed_string.chomp!(@IP_Range.separator)
    end
  end
  
  def to_remove?(section, section_to_follow, section_after_that = nil)
    last_section = section.split(@IP_Range.separator)[-1] rescue   false
    
    if (last_section)
      if (last_section.length % @IP_Range.size_of_sections != 0)
        true
      else
        last_section?(section_to_follow, section_after_that)
      end
    end
  end
  
  def last_section?(section_to_follow, section_after_that)
    if (section_to_follow)
      false
    else
      if (section_after_that)
        false
      else
        true
      end
    end
  end
end
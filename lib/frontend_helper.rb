require File.join(File.dirname(__FILE__),'ip_range.rb')

class FrontendHelper

  @@Invalid_input_string = "invalid input"
  @IP_Range

  def initialize(ip_range)
    @IP_Range = ip_range
  end

  def dotted_hash
    hash = @IP_Range.split
    
    if (not hash)
      nil
    else
      net_string = hash[:net].join unless hash[:net].length == 0
      mixed_string = hash[:mixed].join unless hash[:mixed].length == 0
      host_string = hash[:host].join unless hash[:host].length == 0
    
      char_count = 0
      insert_count = 0
    
      nl = net_string.length rescue 0
      ml = mixed_string.length rescue 0
      hl = host_string.length rescue 0
    
      while char_count+insert_count <= (nl + ml + hl + insert_count - @IP_Range.size_of_sections)
        char_count = char_count+1
        if (char_count % @IP_Range.size_of_sections == 0)
          insert_in_right_string(net_string, mixed_string, host_string, char_count+insert_count)
          insert_count = insert_count+1
        end
      end
      {:net => net_string, :mixed => mixed_string, :host => host_string}
    end
  end
  
  def html_formated_address(empty)
    hash = dotted_hash rescue nil
    
    if error?(hash,empty)
      "<span class='address_error_style' id='address_error'>#{@@Invalid_input_string}</span>"
    else
      if hash
        net_string = hash[:net]
        mixed_string = hash[:mixed]
        host_string = hash[:host]
      end
      "<span class='net_style' id='net'>#{net_string}</span><span class='mixed_style' id='mixed'>#{mixed_string}</span><span class='host_style' id='host'>#{host_string}</span>"
    end
  end
  
  def error?(hash=dotted_hash, empty)
    !(hash || empty)
  end
  
  private
    # insert the separator at the right position in the right string
    # example
    #      net              host
    # |----:----:|-|---:----:----:----|
    #
    def insert_in_right_string(net_string, mixed_string, host_string, count)
      
      nl = net_string.length rescue 0
      ml = mixed_string.length rescue 0
      hl = host_string.length rescue 0
      
      #don't insert at the very end
      # if count >= (nl + ml + hl)
      #   return
      # end

      if count <= nl
        net_string.insert(count,@IP_Range.separator)
      elsif count <= nl + ml
        mixed_string.insert(count - nl, @IP_Range.separator)
      else
        host_string.insert(count - nl - ml, @IP_Range.separator)
      end
    end
end